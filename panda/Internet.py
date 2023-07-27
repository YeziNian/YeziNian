import math
with open(r"C:\Users\40437\Desktop\wandou.txt", "r") as fp:
    data = fp.readline().split()
    lie = []
    label = []
    while data:
        lie.append(list(map(lambda x: eval(x), data[:-1])))
        label.append(int(data[-1]))
        data = fp.readline().split()
def calc_entropy(data):
    """计算信息熵"""
    counts = {}
    for record in data:
        label = record[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    entropy = 0
    for label in counts:
        prob = counts[label] / len(data)
        entropy -= prob * math.log2(prob)
    return entropy

def split_data(data, axis, value):
    """划分数据集"""
    sub_data = []
    for record in data:
        if record[axis] == value:
            sub_record = record[:axis]
            sub_record.extend(record[axis+1:])
            sub_data.append(sub_record)
    return sub_data

def choose_feature(data):
    """选择最佳特征"""
    num_feat = len(data[0]) - 1
    base_entropy = calc_entropy(data)
    best_info_gain = 0
    best_feat = -1
    for i in range(num_feat):
        feat_vals = [record[i] for record in data]
        uniq_vals = set(feat_vals)
        new_entropy = 0
        for val in uniq_vals:
            sub_data = split_data(data, i, val)
            prob = len(sub_data) / len(data)
            new_entropy += prob * calc_entropy(sub_data)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feat = i
    return best_feat

def majority_count(labels):
    """返回出现次数最多的类别"""
    counts = {}
    for label in labels:
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    return sorted_counts[0][0]

def create_tree(data, labels):
    """创建决策树"""
    class_list = [record[-1] for record in data]
    # 类别全部相同，停止递归，返回该类别
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 特征全部遍历完，停止递归，返回出现次数最多的类别
    if len(data[0]) == 1:
        return majority_count(class_list)
    # 选择最佳特征
    best_feat = choose_feature(data)
    best_feat_label = labels[best_feat]
    # 创建决策树
    decision_tree = {best_feat_label: {}}
    del(labels[best_feat])
    feat_vals = [record[best_feat] for record in data]
    uniq_vals = set(feat_vals)
    for val in uniq_vals:
        sub_labels = labels[:]
        sub_data = split_data(data, best_feat, val)
        decision_tree[best_feat_label][val] = create_tree(sub_data, sub_labels)
    return decision_tree
print(create_tree(lie, label))