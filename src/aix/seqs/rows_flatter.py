import numpy as np

class RowsFlatter:
    def __init__(self, rows):
        self._rows = rows
        self._flatted_rows = None

    def get_flatted_rows(self)->np.ndarray:
        #@todo just one nested level is covered
        if self._flatted_rows is None:
            self._flatted_rows = []
            if isinstance(self._rows, np.ndarray):
                for row in self._rows:
                    new_row = []
                    for member in row:
                        if isinstance(member, (float,int,str)):
                            new_row.append(member)
                        elif isinstance(member,np.ndarray):
                            for member_of_member in member:
                                new_row.append(member_of_member)
                    self._flatted_rows.append(new_row)

        return self._flatted_rows

