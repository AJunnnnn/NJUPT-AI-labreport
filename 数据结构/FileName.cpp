#define OK 1
#define WRONG -1
typedef int TElemType;
typedef int Status;

#include<iostream>
using namespace std;


//定义二叉树的结构类型
typedef struct BiNode
{
	TElemType   data;
	struct  BiNode* lchild, * rchild; //左右孩子指针
}BiNode, * BiTree;

//建立二叉树
void CreateBiTree(BiTree& T)
{
	int ch;
	cin >> ch;
	if (ch == 0)   T = NULL;  	//递归结束，建空树
	else
	{
		T = new BiNode;
		T->data = ch; 	//生成根结点
		CreateBiTree(T->lchild);  //递归创建左子树
		CreateBiTree(T->rchild); //递归创建右子树
	}
}


//中序遍历
Status InOrderTraverse(BiTree T) 
{
	if (T == NULL) return OK; //空二叉树
	else {
		InOrderTraverse(T->lchild); //递归遍历左子树
		cout << T->data; //访问根结点
		InOrderTraverse(T->rchild); //递归遍历右子树
	}
}

Status Find(BiTree &T,int k,int value)
{
	if (T == NULL) return OK; //空二叉树
	else {
		Find(T->lchild,k,value); //递归遍历左子树
		if (T->data == k)
		{
			if (T->lchild == NULL)
			{
				BiNode* p = new BiNode;
				p->data = value;
				p->lchild = NULL;
				p->rchild = NULL;
				T->lchild = p;
				return OK;
			}
			else
			{
				if (T->rchild == NULL)
				{
					BiNode* p = new BiNode;
					p->data = value;
					p->lchild = NULL;
					p->rchild = NULL;
					T->rchild = p;
					return OK;
				}
				else
					return WRONG;
			}
		}
		Find(T->rchild,k,value); //递归遍历右子树
	}
}




int main()
{
	int k, value, j;
	BiTree T;
	cout << "首先输入根结点的值，再依次输入左孩子和右孩子的值，如果该结点的左孩子或右孩子为NULL，则输入数字0." << endl;
	CreateBiTree(T);
	InOrderTraverse(T);
	cout << endl;
	cout << "插入的结点和插入的元素：" << endl;
	cin >> k >> value;
	j = Find(T, k, value);
	if (j == OK)
	{
		cout << "中序遍历结果为：" << endl;
		InOrderTraverse(T);
	}
	else
		cout << "该结点左右孩子都已存在！" << endl;
	return 0;
}