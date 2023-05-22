//栈的顺序表示
#include<iostream>
using namespace std;

#define ERROR 0
#define OVERFLOW 0
#define OK 1
typedef int SElemType;
typedef int Status;

#define  MAXSIZE  100
typedef struct
{
	SElemType* base;  //栈底指针
	SElemType* top;   //栈顶指针
	int stacksize;  //栈的容量
}SqStack;


//顺序栈的初始化
Status InitStack(SqStack &S)
{
	S.base = new SElemType[MAXSIZE];
		if (!S.base) 	return OVERFLOW;
	S.top = S.base;
	S.stacksize = MAXSIZE;
	return OK;
}


//判断是否为空
bool StackEmpty(SqStack S)
{
	if (S.top == S.base) return true;
	else return false;
}


//进栈
Status Push(SqStack &S, SElemType e)
{
	if (S.top - S.base == S.stacksize) // 栈满
		return ERROR;
	*S.top++ = e;
	return OK;
}


//出栈
Status Pop(SqStack &S, SElemType &e)
{
	if (S.top == S.base) // 栈空
		return ERROR;
	e=*(--S.top);  //栈顶指针减1，将栈顶元素赋给e
	return OK;
}


//取栈顶元素
Status GetTop(SqStack S, SElemType &e)
{
	if (S.top == S.base)	 return ERROR; 	// 栈空
	e = *(S.top-1);    //返回栈顶元素的值，栈顶指针不变
	return OK;
}


//打印顺序栈
void PrintStack(SqStack S)
{
	if (S.top == S.base)
		cout << "栈为空，无法打印！" << endl;
	else
	{
		int count;
		cout << "该顺序栈的内容为:" << endl;
		SElemType* p = new SElemType;
		p = S.top;
		for(count=0;count<S.top-S.base;count++)
		{
			p = p - 1;
			cout << *p << endl;
		}
	}

}


int main()
{
	SqStack S;
	int choice;
	int x,e;
	InitStack(S);
	cout << "请输入栈中等数据元素的个数：" << endl;
	int n,elem;
	cin >> n;
	int i;
	for (i = 0; i < n; i++)
	{
		cout << "请输入数据元素：";
		cin >> elem;
		Push(S, elem);
	}
	PrintStack(S);
	do {
		cout << "----------------------" << endl;
		cout << "1.加入元素" << endl;
		cout << "2.取出元素" << endl;
		cout << "3.判断非空" << endl;
		cout << "4.初始化" << endl;
		cout << "0.退出" << endl;
		cout << "选择您的操作：" << endl;
		cin >> choice;
		switch(choice)
		{
		case 1:
			cout << "请输入加入的元素" << endl;
			cin >> x;
			Push(S, x);
			PrintStack(S);
			continue;
		case 2:
			Pop(S, e);
			PrintStack(S);
			cout << "取出元素为：" << e << endl;
			continue;
		case 3:
			if (StackEmpty(S) == true)
				cout << "顺序栈为空" << endl;
			else
				cout << "顺序栈非空" << endl;
			continue;
		case 4:
			InitStack(S);
			PrintStack(S);
			continue;
		case 0:
			break;
		}
	} while (choice != 0);


	return 0;
}