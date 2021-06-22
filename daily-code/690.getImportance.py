"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):

    def _getImportance(self, id):
        emp = self.emp_map[id]
        sum_importance = emp.importance
        if not emp.subordinates:
            return sum_importance
        for sub_ordinate in emp.subordinates:
            sum_importance = sum_importance + self._getImportance(sub_ordinate)
        return sum_importance 
            

    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        self.emp_map = {employee.id: employee for employee in employees}
        return self._getImportance(id)