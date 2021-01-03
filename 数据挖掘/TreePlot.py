import matplotlib.pyplot  as plt

# 定义决策树决策结果的属性，用字典来定义

# 下面的字典定义也可写作 decisionNode={boxstyle:'sawtooth',fc:'0.8'}


decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细

leafNode = dict(boxstyle="round4", fc="0.8")  # 定义决策树的叶子结点的描述属性

arrow_args = dict(arrowstyle="<-")  # 定义决策树的箭头属性


def plotNode(nodeTxt, centerPt, parentPt, nodeType):  # 绘制结点

    # annotate是关于一个数据点的文本

    # nodeTxt为要显示的文本，centerPt为文本的中心点，箭头所在的点，parentPt为指向文本的点

    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def getNumLeafs(myTree):  # 获得决策树的叶子结点数目

    numLeafs = 0  # 定义叶子结点数目

    firstStr = list(myTree.keys())[0]  # 获得myTree的第一个键值，即第一个特征，分割的标签

    secondDict = myTree[firstStr]  # 根据键值得到对应的值，即根据第一个特征分类的结果

    for key in secondDict.keys():  # 遍历得到的secondDict

        if type(secondDict[key]).__name__ == 'dict':  # 如果secondDict[key]为一个字典，即决策树结点

            numLeafs += getNumLeafs(secondDict[key])  # 则递归的计算secondDict中的叶子结点数，并加到numLeafs上

        else:  # 如果secondDict[key]为叶子结点

            numLeafs += 1  # 则将叶子结点数加1

    return numLeafs  # 返回求的叶子结点数目


def getTreeDepth(myTree):  # 获得决策树的深度

    maxDepth = 0  # 定义树的深度

    firstStr = list(myTree.keys())[0]  # 获得myTree的第一个键值，即第一个特征，分割的标签

    secondDict = myTree[firstStr]  # 根据键值得到对应的值，即根据第一个特征分类的结果

    for key in secondDict.keys():

        if type(secondDict[key]).__name__ == 'dict':  # 如果secondDict[key]为一个字典

            thisDepth = 1 + getTreeDepth(secondDict[key])

            # 则当前树的深度等于1加上secondDict的深度，只有当前点为决策树点深度才会加1

        else:  # 如果secondDict[key]为叶子结点

            thisDepth = 1  # 则将当前树的深度设为1

        if thisDepth > maxDepth:  # 如果当前树的深度比最大数的深度

            maxDepth = thisDepth

    return maxDepth  # 返回树的深度


def plotMidText(cntrPt, parentPt, txtString):  # 绘制中间文本

    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]  # 求中间点的横坐标

    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]  # 求中间点的纵坐标

    createPlot.ax1.text(xMid, yMid, txtString)  # 绘制树结点  (函数)


def plotTree(myTree, parentPt, nodeTxt):  # 绘制决策树

    numLeafs = getNumLeafs(myTree)  # 定义并获得决策树的叶子结点数

    depth = getTreeDepth(myTree)  # 定义并获得决策树的深度

    firstStr = list(myTree.keys())[0]  # 得到第一个特征

    # 计算坐标，x坐标为当前树的叶子结点数目除以整个树的叶子结点数再除以2，y为起点

    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)

    # 绘制中间结点，即决策树结点，也是当前树的根结点，这句话没感觉出有用来，

    plotMidText(cntrPt, parentPt, nodeTxt)

    plotNode(firstStr, cntrPt, parentPt, decisionNode)  # 绘制决策树结点

    secondDict = myTree[firstStr]  # 根据firstStr找到对应的值

    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD  # 因为进入了下一层，所以y的坐标要变 ，图像坐标是从左上角为原点

    for key in secondDict.keys():  # 遍历secondDict

        if type(secondDict[key]).__name__ == 'dict':  # 如果secondDict[key]为一棵子决策树，即字典

            plotTree(secondDict[key], cntrPt, str(key))  # 递归的绘制决策树

        else:  # 若secondDict[key]为叶子结点

            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW  # 计算叶子结点的横坐标

            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)  # 绘制叶子结点

            # 这句注释掉也不影响决策树的绘制,自己理解的浅陋了，这行代码是特征的值

            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))

    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD  # 计算纵坐标


def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')  # 定义一块画布(画布是自己的理解)

    fig.clf()  # 清空画布

    axprops = dict(xticks=[], yticks=[])  # 定义横纵坐标轴，无内容

    createPlot.ax1 = plt.subplot(111, frameon=True, **axprops)  # 绘制图像，无边框，无坐标轴

    plotTree.totalW = float(getNumLeafs(inTree))  # plotTree.totalW保存的是树的宽

    plotTree.totalD = float(getTreeDepth(inTree))  # plotTree.totalD保存的是树的高

    plotTree.xOff = - 0.5 / plotTree.totalW  # 从0开始会偏右  #决策树起始横坐标

   # print(plotTree.xOff)

    plotTree.yOff = 1.0  # 决策树的起始纵坐标

    plotTree(inTree, (0.5, 1.0), '')  # 绘制决策树

    plt.show()  # 显示图像