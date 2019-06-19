class ListHelper:
    """
        列表助手:定义列表的常用操作.
    """

    @staticmethod
    def find(list_target, func):
        """
            在列表中根据指定条件查找所有元素
        :param list_target: 目标列表
        :param func: 查找条件
        :return: 生成器对象
        """
        for item in list_target:
            if func(item):
                yield item

    @staticmethod
    def first(list_target, func):
        """
            获取列表中第一个满足条件的元素
        :param list_target: 目标列表
        :param func: 满足条件
        :return: 返回元素
        """
        for item in list_target:
            if func(item):
                return item

    @staticmethod
    def get_count(list_target, func):
        """
            获取列表中满足条件的元素数量
        :param list_target: 目标列表
        :param func: 满足条件
        :return: 数量
        """
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def get_sum(list_target, func):
        """
            自定义类的列表求和
        :param list_target: 目标列表
        :param func: 元素的处理逻辑
        :return: 总和
        """
        sum = 0
        for item in list_target:
            sum += func(item)
        return sum

    @staticmethod
    def get_max(list_target, func):
        """
            在列表中获取满足条件的最大元素
        :param list_target: 目标列表
        :param func: 条件
        :return: 最大元素
        """
        max = list_target[0]
        for i in range(1, len(list_target)):
            if func(max) < func(list_target[i]):
                max = list_target[i]
        return max
    @staticmethod
    def get_min(list_target, func):
        """
            在列表中获取满足条件的最小元素
        :param list_target: 目标列表
        :param func: 条件
        :return: 最小元素
        """
        min = list_target[0]
        for i in range(1, len(list_target)):
            if func(min) > func(list_target[i]):
                min = list_target[i]
        return min

    @staticmethod
    def select(list_target, func):
        """
            根据条件，筛选列表
        :param list_target: 目标列表
        :param func: 条件
        :return: 需要的数据组成的列表
        """
        list0 = []
        for item in list_target:
            list0.append(func(item))
        return list0

    @staticmethod
    def order_by(list_target, func):
        """
            根据条件对列表进行升序排列
        :param list_target: 目标列表
        :param func: 排序条件
        :return:
        """

        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func(list_target[r]) > func(list_target[c]):
                    list_target[r], list_target[c] = \
                        list_target[c], list_target[r]

