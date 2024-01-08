def label_district(data):
    dis = sorted(data['Quận'].unique())
    lb_dis = {}

    for i, j in enumerate(dis):
        lb_dis[j] = i
        
    return lb_dis

def label_street(data):
    street = sorted(data['Đường'].unique())
    lb_street = {}

    for i, j in enumerate(street):
        lb_street[j] = i
        
    return lb_street

def convert(label_district, label_street, val):
    if val in label_district.keys():
        return label_district[val]
    else:
        return label_street[val]