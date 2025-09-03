import copy 

class Alter:
    __name: str = ''
    __params: dict = {'weight': 85, 'height':185}

    def __init__(self, donor: 'Alter' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    
    def set_name(self,name: str):
        self.__name = name 
    
    def get_name(self) ->str:
        return self.__name
    
    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, new_weight: int):
        self.__params['weight'] = new_weight
    
    def set_height(self, new_height: int):
        self.__params['height'] = new_height

    def clone(self):
        return Alter(self)
    
if __name__ == '__main__':
    alter_donor: Alter = Alter()
    alter_donor.set_name('Anton')

    alter_clone: Alter = alter_donor.clone()
    
    print('Donor:', alter_donor.get_name(), alter_donor.get_params())
    print('Clone:', alter_clone.get_name(), alter_clone.get_params())

    alter_clone.set_weight(80)
    alter_clone.set_height(186)
    alter_clone.set_name('Alter_Anton_2.0')
    print()

    print('Donor:', alter_donor.get_name(), alter_donor.get_params())
    print('Clone:', alter_clone.get_name(), alter_clone.get_params())

    