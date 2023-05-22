#include<iostream>
#include<fstream>
#include<string>
using namespace std;

#define ERROR 0
#define OK 1
typedef int ElemType;
typedef int Status;


typedef struct LNode
{
    ElemType   data;      
    struct LNode* next;   
}LNode, * LinkList;

//��ʼ��
Status InitList_L(LinkList& L)
{
    L = new LNode;
    L->next = NULL;
    return OK;
}

//��������
int  ListLength_L(LinkList L)
{
    int i = 0;
    LinkList p;
    p = L->next;       
    while (p) 
    {
        i++;
        p = p->next;
    }
    return i;
}

//�ж������Ƿ�Ϊ��
int ListEmpty(LinkList L)
{
    if (L->next)  
        return 0;
    else
        return 1;
}

//��ѯԪ��
Status GetElem_L(LinkList L, int i, ElemType& e)
{
    LinkList p;
    p = L->next;
    int j = 1; 
    while (p && j < i) 
    {
        p = p->next; ++j;
    }
    if (!p || j > i)return ERROR;  
    e = p->data; 
    return OK;
}

//����
Status ListInsert_L(LinkList& L, int i, ElemType e)
{
    LinkList p = L;
    int j = 0;
    while (p && j < i - 1) { p = p->next; ++j; }	
    if (!p || j > i - 1)return ERROR;	 
    LNode* s = new LNode;			
    s->data = e;      		          
    s->next = p->next;	   	          
    p->next = s;
    return OK;
}

//ɾ��
Status ListDelete_L(LinkList& L, int i, ElemType& e) {
    LinkList p = L;
    int j = 0;
    while (p->next && j < i - 1) {                 
        p = p->next; ++j;
    }
    if (!(p->next) || j > i - 1) return ERROR; 
    LNode* q = p->next;                                      
    p->next = q->next; 	                  
    e = q->data; 	                             
    delete q; 	                              
    return OK;
}

//ǰ���������
void CreateList_F(LinkList& L, int n) {
    int i;
    L = new LNode;
    L->next = NULL; 
    for (i = n; i > 0; --i) {
        LNode* p = new LNode; 
        cin >> p->data; 
        p->next = L->next; L->next = p; 	
    }
}

//�������
void ListOutput(LinkList L) 
{
    LinkList p;
    p = L->next;
    while (p != NULL) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

//���������Ͻ���
LinkList Getjiaolist(LinkList LA, LinkList LB, LinkList LC)
{
    LinkList p, q, p1;
    p = LA->next;
    //LA->next = NULL;
    p1 = LC;
    q = LB->next;
    while (p)
    {
        if (p->data == q->data)
        {
            LinkList a;
            a = new LNode;   //����һ���½��
            if (a == NULL)
            {
                cout << "error";
                exit(0);
            }
            else a->next = NULL;
            a->data = p->data;
            a->next = NULL;
            p1->next = a;
            p1 = a;
            p = p->next;
            q = LB->next;
        }
        else
        {
            if (q->next != NULL)q = q->next;
            else
            {
                p = p->next;
                q = LB->next;
            }
        }
    }
    return LC;
}



int main()
{
    LinkList L1;
    LinkList L2;
    LinkList LC;
    InitList_L(L1);
    InitList_L(L2);
    InitList_L(LC);
    int n;
    cout << "���뽨��������L1��Ԫ�ظ����ǣ�" << endl;
    cin >> n;
    cout << "����������Ԫ��" << endl;
    CreateList_F(L1, n);
    cout << "�������ĵ�����L1Ϊ��" << endl;
    ListOutput(L1);
 //   int count = ListLength_L(L1);
 //   cout << "Ԫ�ظ���Ϊ��" << count;
 //   ListInsert_L(L1, 3, 3);
 //   cout << "����Ԫ�غ�����Ϊ��" << endl;
 //   ListOutput(L1);
 //   int e ;
 //   ListDelete_L(L1, 2, e);
 //   cout << "ɾ��Ԫ�غ�����Ϊ��" << endl;
 //   ListOutput(L1);
 //   GetElem_L(L1, 4, e);
 //   cout << "��Ԫ��Ϊ��" << e << endl;
 //   e=ListEmpty(L1);
 //   if (e == 1){cout << "������Ϊ�գ�" << endl; }
 //   else cout << "������ǿգ�" << endl;
    cout << "���뽨��������L2��Ԫ�ظ����ǣ�" << endl;
    cin >> n;
    cout << "����������Ԫ��" << endl;
    CreateList_F(L2, n);
    cout << "�������ĵ�����L2Ϊ��" << endl;
    ListOutput(L2);
    LC = Getjiaolist(L1, L2,LC);
    cout << "L1��L2�Ľ���Ϊ��" << endl;
    ListOutput(LC);

    return 0;
}