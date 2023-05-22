#include <iostream>
using namespace std;


#define OK 1
#define ERROR 0
#define MVNum 100                       //最大顶点数 
typedef int Status;
typedef int VerTexType;              	//假设顶点的数据类型为int
typedef int ArcType;                  	//假设边的权值类型为int

typedef struct {
	VerTexType vexs[MVNum];            		//顶点表 
	ArcType arcs[MVNum][MVNum];      	    //邻接矩阵 
	int vexnum, arcnum;                		//图的当前点数和边数 
}AMGraph;


int LocateVex(AMGraph G, VerTexType u)
{//存在则返回u在顶点表中的下标;否则返回-1
    int i;
    for (i = 0; i < G.vexnum; ++i)
        if (u == G.vexs[i]) //判断u是否在顶点表中
            return i;
    return -1;
}

Status CreateUDN(AMGraph &G) {
    //采用邻接矩阵表示法，创建无向网G 
    int i,j,k;
    VerTexType v1, v2;
    cout << "请输入总顶点数和总边数：" << endl;
    cin >> G.vexnum >> G.arcnum; 	//输入总顶点数，总边数 
    if (G.arcnum > (G.vexnum*(G.vexnum-1))/2)
        return ERROR;

    for (i = 0; i < G.vexnum; ++i)
    {
        cout << "请输入第" << (i + 1) << "个点的名称(数据类型均为int):";
        cin >> G.vexs[i];
    }//依次输入点的信息，顶点表

    for (i = 0; i < G.vexnum; ++i) 	//初始化邻接矩阵，边的权值均置为极大值
    {
        for (j = 0; j < G.vexnum; ++j)
            G.arcs[i][j] = 0;
    }

    for (k = 0; k < G.arcnum; ++k) 
    {                     
        //构造邻接矩阵 
        cout << "请输入第" << (k + 1) << "条边依附的顶点:" << endl;
        cin >> v1 >> v2 ;         //输入一条边依附的顶点及权值 
        i = LocateVex(G, v1);
        j = LocateVex(G, v2);          //确定v1和v2在顶点表中的位置
        G.arcs[i][j] = 1;                   //边<v1, v2>的权值设置为w 
        G.arcs[j][i] = G.arcs[i][j];    //设置<v1, v2>的对称边<v2, v1>的权值为w 
    }
    return OK;
}


//深度优先搜索
bool visited[MVNum];
void DFS(AMGraph G, int v) 
{
    cout << G.vexs[v-1]<<"\t";  
    visited[v] = true;  		//访问第v个顶点
    for (int w = 1; w <= G.vexnum; w++)  	//依次检查邻接矩阵v所在的行  
    {
        if ((G.arcs[v-1][w-1] != 0) && (!visited[w]))
            DFS(G, w);
    }
    //w是v的邻接点，如果w未访问，则递归调用DFS 
}

void PrintGraph(AMGraph G)
{
    int i;
    int j;
    cout << "------以下为创建的图------" << endl;
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
    cout << "------以上为创建的图------" << endl;
}


int main()
{
    int x;
    AMGraph  G;
    x = CreateUDN(G);
    if (x == 1)
    {
        cout << "无向图创建成功！" << endl;
        PrintGraph(G);
        cout << "以下为深度优先遍历后的结果：" << endl;
        DFS(G, 2);
    }
    else
    {
        cout << "无向图创建失败！" << endl;
    }
    
	return 0;
}