//ջ��˳���ʾ
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
	SElemType* base;  //ջ��ָ��
	SElemType* top;   //ջ��ָ��
	int stacksize;  //ջ������
}SqStack;


//˳��ջ�ĳ�ʼ��
Status InitStack(SqStack &S)
{
	S.base = new SElemType[MAXSIZE];
		if (!S.base) 	return OVERFLOW;
	S.top = S.base;
	S.stacksize = MAXSIZE;
	return OK;
}


//�ж��Ƿ�Ϊ��
bool StackEmpty(SqStack S)
{
	if (S.top == S.base) return true;
	else return false;
}


//��ջ
Status Push(SqStack &S, SElemType e)
{
	if (S.top - S.base == S.stacksize) // ջ��
		return ERROR;
	*S.top++ = e;
	return OK;
}


//��ջ
Status Pop(SqStack &S, SElemType &e)
{
	if (S.top == S.base) // ջ��
		return ERROR;
	e=*(--S.top);  //ջ��ָ���1����ջ��Ԫ�ظ���e
	return OK;
}


//ȡջ��Ԫ��
Status GetTop(SqStack S, SElemType &e)
{
	if (S.top == S.base)	 return ERROR; 	// ջ��
	e = *(S.top-1);    //����ջ��Ԫ�ص�ֵ��ջ��ָ�벻��
	return OK;
}


//��ӡ˳��ջ
void PrintStack(SqStack S)
{
	if (S.top == S.base)
		cout << "ջΪ�գ��޷���ӡ��" << endl;
	else
	{
		int count;
		cout << "��˳��ջ������Ϊ:" << endl;
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
	cout << "������ջ�е�����Ԫ�صĸ�����" << endl;
	int n,elem;
	cin >> n;
	int i;
	for (i = 0; i < n; i++)
	{
		cout << "����������Ԫ�أ�";
		cin >> elem;
		Push(S, elem);
	}
	PrintStack(S);
	do {
		cout << "----------------------" << endl;
		cout << "1.����Ԫ��" << endl;
		cout << "2.ȡ��Ԫ��" << endl;
		cout << "3.�жϷǿ�" << endl;
		cout << "4.��ʼ��" << endl;
		cout << "0.�˳�" << endl;
		cout << "ѡ�����Ĳ�����" << endl;
		cin >> choice;
		switch(choice)
		{
		case 1:
			cout << "����������Ԫ��" << endl;
			cin >> x;
			Push(S, x);
			PrintStack(S);
			continue;
		case 2:
			Pop(S, e);
			PrintStack(S);
			cout << "ȡ��Ԫ��Ϊ��" << e << endl;
			continue;
		case 3:
			if (StackEmpty(S) == true)
				cout << "˳��ջΪ��" << endl;
			else
				cout << "˳��ջ�ǿ�" << endl;
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