## numpy
# 创建一个一维的数组 lst= np.arange(1, 13)
结果是[ 1  2  3  4  5  6  7  8  9 10 11 12]

reshape([3, 4])表示把已经产生的一维数组重新改变结构变成3行4列
np.array([[1, 2., 5], [4, 5, 6], [5, 9, 6]])也可以产生一个3行3列的元组
数组的转置lst.transpose()
列表（矩阵求和）det(lst)
数组.shape可以得到数组的列和行
数组.size可以得到数组元素的个数
数组.dtype可以得到数组的数据类型
np.zeros([2, 5])创建2行5列的全0的矩阵
np.eye(3)创建一个3行3列的单位矩阵
np.random.randn(10)创建随机正态分布图
np.random.randint(10, size=10)随机生成10个一维数组
np.unique(a)得到矩阵中的唯一值是那些
# 把随机产生的元组保存到本地
f = open('x.pkl', 'wb')
# 把x保存到发中
pickle.dump(x, f)
## DataFrame
# 取出df中列是employee_no，real_name，give_workld的属性
df_new = DataFrame(df, columns=['employee_no', 'real_name', 'give_workld'])
print(df_new)

# 新增一列study 默认值全是NaN
df_new = DataFrame(df, columns=['employee_no', 'real_name', 'give_workld', 'study'])
print(df_new)
# 给新增的study添加数据,有序添加1到10的数据
df_new['study'] = range(1, 10)
df_new['study']= np.arange(1,10)
df_new['study']=pd.Series(np.arange(1,10))
print(df_new)
# 只填充index
df_new['study']=pd.Series([100,200],index=[1,2])为1和2的列，
# excel-->csv
df = pd.read_excel(r'Data.xlsx')
df.to_csv('df.csv')
# 读取csv文件内容
df1 = pd.read_csv('df.csv')
print(df1)
# csv-->json
df1.to_json
# json--->csv
pd.read_json(df1.to_json())
# csv-->html
df1.to_html('df1.html')
# csv-->excel
df1.to_excel('df1.xlsx')
# io文件流 
sub_df = df5[['employee_no', 'real_name', 'employee_unit']]
s = sub_df.loc[3:8, :]
# 输出lable 3--8行的数据
print(s)
s1 = s.loc[7:7, :]
# 得到s1中employee_unit的值
s1['employee_unit']

# 序列化
n1 = pd.Series([[5, 6, 7, 8], [1, 2, 3, 4]])
序列化后的值是一个元组

n4 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
A    1
B    2
C    3
D    4
n4.to_dict() 序列化后的值直接转换为字典

#reindex
s1 = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# 在缺失值的E位置上添加值10
s2 = s1.reindex(index=['A','B','C','D','E'],fill_value=10)
df1 = DataFrame(np.random.rand(25).reshape([5,5]),index=['A', 'B', 'D', 'E', 'F'],columns = ['c1', 'c2', 'c3', 'c4', 'c5'])
# 得到行A\C
df4 = df1.reindex(index=['A', 'C'])
# 删除行B
df1.drop(index='B')
# 删除列c2,c5
df1.drop(columns=['c2', 'c5'])

####DataFrame是二维的，Series是一维的
# 可以直接用字典创建一个DataFrame 
eg:df1=DateFrame({'城市':['北京','上海','广州'],'人口':[1000,1500,2000]})
# 利用df1['GDP']=Series([1000,2000,3000])可以直接添加一columns GDP
或者利用map函数
#把index为1的替换为np.nan s1.replace({1:np.nan})
# 创建一个5*5的矩阵 
df1 = DataFrame(np.random.rand(25).reshape([5, 5]), index=['A', 'B', 'D', 'E', 'F'],
                columns=['c1', 'c2', 'c3', 'c4', 'c5'])


print('DataFrame排序：')
df = DataFrame(np.random.randn(40).reshape([8, 5]), columns=['A', 'B', 'C', 'D', 'E'])
print(df)
# 根据A的index进行排序（只排序A）
print(df['A'].sort_index())
# 根据A排序所有的数据
print(df.sort_value('A))
# 重命名
df1.rename(index=str.lower,columns=str.lower)
df2 = df1.rename(index={'BJ':'北京'},columns = {'A':'a'})
# 使用列表解析直接把lst=[1,2,3,4]转换为lst=['1','2','3','4']
lst = [str(x) for x in lst]
df1 = DateFrame({'key':['A','B','C','D'],'value':[1,2,3,4,5]})
"""# Concatenate和Combine"""
arr1 = np.arange(9).reshape([3,3])
arr2 = np.arange(9).reshape([3,3])
# 可以直接用del直接删除一个行的值
# del df['Unnamed: 0']
# # 删除重复值
# print(df['Seqno'].drop_duplicates())
# # 删除重复行
# print(df.drop_duplicates(['Seqno'],keep='last'))
#透视表
df = pd.read_excel('excel所在目录')
df.to_csv('转换后的csv文件名')
# csv---->透视表
print(pd.pivot_table(df,index=['Manager','Rep'],values=['Price', 'Quantity'], fill_value=0, columns=['Product'],
  aggfunc='sum'))











