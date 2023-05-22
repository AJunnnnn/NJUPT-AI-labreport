#define OK 1
#define WRONG -1
typedef int TElemType;
typedef int Status;

#include<iostream>
using namespace std;


//����������Ľṹ����
typedef struct BiNode
{
	TElemType   data;
	struct  BiNode* lchild, * rchild; //���Һ���ָ��
}BiNode, * BiTree;

//����������
void CreateBiTree(BiTree& T)
{
	int ch;
	cin >> ch;
	if (ch == 0)   T = NULL;  	//�ݹ������������
	else
	{
		T = new BiNode;
		T->data = ch; 	//���ɸ����
		CreateBiTree(T->lchild);  //�ݹ鴴��������
		CreateBiTree(T->rchild); //�ݹ鴴��������
	}
}


//�������
Status InOrderTraverse(BiTree T) 
{
	if (T == NULL) return OK; //�ն�����
	else {
		InOrderTraverse(T->lchild); //�ݹ����������
		cout << T->data; //���ʸ����
		InOrderTraverse(T->rchild); //�ݹ����������
	}
}

Status Find(BiTree &T,int k,int value)
{
	if (T == NULL) return OK; //�ն�����
	else {
		Find(T->lchild,k,value); //�ݹ����������
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
		Find(T->rchild,k,value); //�ݹ����������
	}
}




int main()
{
	int k, value, j;
	BiTree T;
	cout << "�������������ֵ���������������Ӻ��Һ��ӵ�ֵ������ý������ӻ��Һ���ΪNULL������������0." << endl;
	CreateBiTree(T);
	InOrderTraverse(T);
	cout << endl;
	cout << "����Ľ��Ͳ����Ԫ�أ�" << endl;
	cin >> k >> value;
	j = Find(T, k, value);
	if (j == OK)
	{
		cout << "����������Ϊ��" << endl;
		InOrderTraverse(T);
	}
	else
		cout << "�ý�����Һ��Ӷ��Ѵ��ڣ�" << endl;
	return 0;
}