class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while sandwiches:
            if sandwiches[0] in students:
                if students[0] != sandwiches[0]:
                    students.append(students[0])
                    del students[0]
                else:
                    del students[0]
                    del sandwiches[0]
            else:
                break           
        
        return len(students)
        
        