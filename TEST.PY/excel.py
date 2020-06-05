import xlwt

def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def make_data(event_list,list1,sheet1,village_id,village_ext_id):
    ses = 3
    if event_list[0] != 0 :
        for i in range(event_list[0]):
            name1 = '户主' + str(i)
            house_id = []
            for p in range(0,event_list[0]):
                house_id.append('0000' + str(p))
            list1 = [name1,village_id,village_ext_id,house_id[i],'男','团员','汉族','360428199602033553','务农','本科','1949-11-30','13012341234','户主']
            for q in range(0,len(list1)):
                sheet1.write(ses,q,list1[q])
            ses = ses + 1
    if event_list[1] != 0 :
        for i in range(event_list[1]):
            name1 = '家庭成员' + str(i)
            house_id = '00001'
            list1 = [name1,village_id,village_ext_id,house_id,'男','团员','汉族','360428199602033553','务农','本科','1949-11-30','13012341234','家庭成员']
            for q in range(0,len(list1)):
                sheet1.write(ses,q,list1[q])
            ses += 1
    else:
        print("数据错误或新增数据为0.")







if __name__ == '__main__':
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet('一户一码', cell_overwrite_ok=True)
    row_list1 = ['姓名(*)','村编号(*)','自然村编号(*)','门牌号(*)','性别(*)','政治面貌(*)','民族(*)','身份证号码','职业(*)','文化程度(*)','出生日期(*)','手机号(*)','和户主关系(*)']
    str1 = '说明：(*)为必填项  示例勿删除   一次只能导入一个行政村 性别(男 ，女)，政治面貌（党员，团员，其他民主党，群众） 职业（务农，商家，本地务工，外地务工,，学生，其他）和户主关系（户主，妻子，丈夫，长子，次子，长女，次女，家庭成员）文化程度 （未入学,幼儿园,小学，初中，高中，大专，本科，研究生，博士）'
    for i in range(0,len(row_list1)):
        sheet1.write(0,i,row_list1[i])


    sheet1.write_merge(1,1,0,12,str1)
    row_list2 = ['张三（示例  ）','4105020001','','xx村1号','男','党员','汉族','','务农','本科','1949-11-30','18888888888','户主']
    for i in range(0,len(row_list2)):
        sheet1.write(2,i,row_list2[i])

    a = int(input("请输入需要新增的户主数量：\n"))
    b = int(input("请输入需要新增的家庭成员数量：\n"))
    event_list = [a,b]
    list1 = []
    village_id='3301060001'
    village_ext_id = 'CSEC1587364525318'
    make_data(event_list,list1,sheet1,village_id,village_ext_id)
    f.save('D:/一户一码.xlsx')



