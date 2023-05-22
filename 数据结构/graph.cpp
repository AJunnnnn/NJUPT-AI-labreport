#include <iostream>
using namespace std;


#define OK 1
#define ERROR 0
#define MVNum 100                       //��󶥵��� 
typedef int Status;
typedef int VerTexType;              	//���趥�����������Ϊint
typedef int ArcType;                  	//����ߵ�Ȩֵ����Ϊint

typedef struct {
	VerTexType vexs[MVNum];            		//����� 
	ArcType arcs[MVNum][MVNum];      	    //�ڽӾ��� 
	int vexnum, arcnum;                		//ͼ�ĵ�ǰ�����ͱ��� 
}AMGraph;


int LocateVex(AMGraph G, VerTexType u)
{//�����򷵻�u�ڶ�����е��±�;���򷵻�-1
    int i;
    for (i = 0; i < G.vexnum; ++i)
        if (u == G.vexs[i]) //�ж�u�Ƿ��ڶ������
            return i;
    return -1;
}

Status CreateUDN(AMGraph &G) {
    //�����ڽӾ����ʾ��������������G 
    int i,j,k;
    VerTexType v1, v2;
    cout << "�������ܶ��������ܱ�����" << endl;
    cin >> G.vexnum >> G.arcnum; 	//�����ܶ��������ܱ��� 
    if (G.arcnum > (G.vexnum*(G.vexnum-1))/2)
        return ERROR;

    for (i = 0; i < G.vexnum; ++i)
    {
        cout << "�������" << (i + 1) << "���������(�������;�Ϊint):";
        cin >> G.vexs[i];
    }//������������Ϣ�������

    for (i = 0; i < G.vexnum; ++i) 	//��ʼ���ڽӾ��󣬱ߵ�Ȩֵ����Ϊ����ֵ
    {
        for (j = 0; j < G.vexnum; ++j)
            G.arcs[i][j] = 0;
    }

    for (k = 0; k < G.arcnum; ++k) 
    {                     
        //�����ڽӾ��� 
        cout << "�������" << (k + 1) << "���������Ķ���:" << endl;
        cin >> v1 >> v2 ;         //����һ���������Ķ��㼰Ȩֵ 
        i = LocateVex(G, v1);
        j = LocateVex(G, v2);          //ȷ��v1��v2�ڶ�����е�λ��
        G.arcs[i][j] = 1;                   //��<v1, v2>��Ȩֵ����Ϊw 
        G.arcs[j][i] = G.arcs[i][j];    //����<v1, v2>�ĶԳƱ�<v2, v1>��ȨֵΪw 
    }
    return OK;
}


//�����������
bool visited[MVNum];
void DFS(AMGraph G, int v) 
{
    cout << G.vexs[v-1]<<"\t";  
    visited[v] = true;  		//���ʵ�v������
    for (int w = 1; w <= G.vexnum; w++)  	//���μ���ڽӾ���v���ڵ���  
    {
        if ((G.arcs[v-1][w-1] != 0) && (!visited[w]))
            DFS(G, w);
    }
    //w��v���ڽӵ㣬���wδ���ʣ���ݹ����DFS 
}

void PrintGraph(AMGraph G)
{
    int i;
    int j;
    cout << "------����Ϊ������ͼ------" << endl;
    cout << "   ";
    for (i = 0; i < G.arcnum; i++)
        cout << G.vexs[i];
    cout << endl;
    for (i = 0; i < G.arcnum; i++)
    {
        cout << G.vexs[i]<<"  ";
        for (j = 0; j < G.arcnum; j++)
            cout << G.arcs[i][j];
        cout << endl;
    }
    cout << "------����Ϊ������ͼ------" << endl;
}


int main()
{
    int x;
    AMGraph  G;
    x = CreateUDN(G);
    if (x == 1)
    {
        cout << "����ͼ�����ɹ���" << endl;
        PrintGraph(G);
        cout << "����Ϊ������ȱ�����Ľ����" << endl;
        DFS(G, 2);
    }
    else
    {
        cout << "����ͼ����ʧ�ܣ�" << endl;
    }
    
	return 0;
}