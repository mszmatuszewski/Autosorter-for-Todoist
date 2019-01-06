import unittest

from autosorter.model import *
from autosorter.spi import *


class TestSort(unittest.TestCase):

    def test_default(self):
        data = [
            Node(Item("A")),
            Node(Item("B", due_date="01 Dec 2018 03:59:59 +0000")),
            Node(Item("C", due_date="01 Dec 2018 01:59:59 +0000")),
            Node(Item("D", due_date="01 Oct 2018 01:59:59 +0000"))
        ]

        result = DefaultSorter()(data)

        self.assertListEqual([data[0], data[3], data[2], data[1]], result)


    def test_project_and_name(self):
        data = [
            Node(Item(name="C", project_id=1)),
            Node(Item(name="A", project_id=2)),
            Node(Item(name="A", project_id=1)),
            Node(Item(name="B", project_id=1))
        ]

        result = SortingBy(project_id).then_by(name)(data)

        self.assertListEqual([data[2], data[3], data[0], data[1]], result)


    def test_full(self):
        data = [
            Node(Item(name="rnlph", id=4, order=1, user_id=5, project_id=4, priority=5, responsible_uid=6)),
            Node(Item(name="pmyof", id=5, order=5, user_id=5, project_id=6, priority=3, responsible_uid=6)),
            Node(Item(name="rqcmw", id=1, order=3, user_id=5, project_id=1, priority=1, responsible_uid=1)),
            Node(Item(name="vxzdk", id=1, order=4, user_id=1, project_id=6, priority=2, responsible_uid=1)),
            Node(Item(name="sdsay", id=3, order=4, user_id=2, project_id=2, priority=1, responsible_uid=4)),
            Node(Item(name="zarnw", id=5, order=5, user_id=3, project_id=3, priority=5, responsible_uid=4)),
            Node(Item(name="fmwbs", id=1, order=1, user_id=3, project_id=4, priority=5, responsible_uid=6)),
            Node(Item(name="nggck", id=5, order=4, user_id=1, project_id=1, priority=3, responsible_uid=3)),
            Node(Item(name="xfpfr", id=4, order=6, user_id=5, project_id=1, priority=3, responsible_uid=2)),
            Node(Item(name="bspne", id=4, order=4, user_id=1, project_id=1, priority=1, responsible_uid=3)),
            Node(Item(name="ymzqj", id=1, order=5, user_id=3, project_id=6, priority=5, responsible_uid=3)),
            Node(Item(name="lyeza", id=2, order=1, user_id=1, project_id=3, priority=5, responsible_uid=6)),
            Node(Item(name="pxykc", id=4, order=6, user_id=1, project_id=6, priority=1, responsible_uid=2)),
            Node(Item(name="ohskw", id=3, order=2, user_id=1, project_id=3, priority=5, responsible_uid=3)),
            Node(Item(name="jfsca", id=1, order=2, user_id=4, project_id=6, priority=5, responsible_uid=4)),
            Node(Item(name="ficcq", id=3, order=5, user_id=4, project_id=1, priority=3, responsible_uid=6)),
            Node(Item(name="aqmsr", id=6, order=1, user_id=2, project_id=4, priority=1, responsible_uid=1)),
            Node(Item(name="drgqc", id=3, order=1, user_id=4, project_id=4, priority=1, responsible_uid=2)),
            Node(Item(name="dvhxz", id=4, order=3, user_id=2, project_id=4, priority=5, responsible_uid=5)),
            Node(Item(name="syiaw", id=4, order=1, user_id=5, project_id=3, priority=3, responsible_uid=3))
        ]

        result = SortingBy(task_id).then_by(item_order).then_by(user_id).then_by(project_id).then_by(name).then_by(priority).then_by(responsible_uid)(data)

        self.assertListEqual([data[6], data[14], data[2], data[3], data[10], data[11], data[17], data[13], data[4], data[15],
                              data[19], data[0], data[18], data[9], data[12], data[8], data[7], data[5], data[1], data[16]], result)
