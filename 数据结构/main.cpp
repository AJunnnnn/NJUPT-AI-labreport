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

//初始化
Status InitList_L(LinkList& L)
{
    L = new LNode;
    L->next = NULL;
    return OK;
}

//求链表长度
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

//判断链表是否为空
int ListEmpty(LinkList L)
{
    if (L->next)  
        return 0;
    else
        return 1;
}

//查询元素
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

//插入
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

//删除
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

//前差法创建链表
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

//输出链表
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

//求两个集合交集
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
            a = new LNode;   //申请一个新结点
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
    cout << "您想建立的链表L1的元素个数是：" << endl;
    cin >> n;
    cout << "请依次输入元素" << endl;
    CreateList_F(L1, n);
    cout << "您创建的单链表L1为：" << endl;
    ListOutput(L1);
 //   int count = ListLength_L(L1);
 //   cout << "元素个数为：" << count;
 //   ListInsert_L(L1, 3, 3);
 //   cout << "插入元素后单链表为：" << endl;
 //   ListOutput(L1);
 //   int e ;
 //   ListDelete_L(L1, 2, e);
 //   cout << "删除元素后单链表为：" << endl;
 //   ListOutput(L1);
 //   GetElem_L(L1, 4, e);
 //   cout << "该元素为：" << e << endl;
 //   e=ListEmpty(L1);
 //   if (e == 1){cout << "该链表为空！" << endl; }
 //   else cout << "该链表非空！" << endl;
    cout << "您想建立的链表L2的元素个数是：" << endl;
    cin >> n;
    cout << "请依次输入元素" << endl;
    CreateList_F(L2, n);
    cout << "您创建的单链表L2为：" << endl;
    ListOutput(L2);
    LC = Getjiaolist(L1, L2,LC);
    cout << "L1和L2的交集为：" << endl;
    ListOutput(LC);

    return 0;
}