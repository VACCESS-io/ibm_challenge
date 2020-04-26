import typing as ty


class CountyInputData:
    def __init__(self, name: str, population: int, doubling_rate: float, doctor_count: int, infected_population: int):
        self.name = name,
        self.population = population
        self.doubling_rate_days = doubling_rate
        self.num_doctor = doctor_count
        self.infected_population = infected_population


class StateInputData:
    def __init__(self, state: str, county_list: ty.List):
        self.state = state
        self.county_list = county_list

    def get_county_data(self):
        return self.county_list


california_county_data = [
                CountyInputData('LosAngeles', 10105518, 15.4, 7397, 12051),
               CountyInputData('SanDiego', 3343364, 19.4, 2664, 2213),
               CountyInputData('SanFransisco', 883305, 18.9, 1366, 1137),
               CountyInputData('Riverside', 2450758, 8.6, 1030, 2602),
               CountyInputData('Orange', 3185968, 19.4, 3108, 1556),
               CountyInputData('SanBernadino', 2171603, 15.3, 1262, 1219),
               CountyInputData('Alameda', 1666753, 14.7, 1832, 1114),
               CountyInputData('SantaClara',1937570, 21.3, 2011, 1870),
               CountyInputData('Kern',896764, 10.2,442,610),
               CountyInputData('SanMateo',769545, 8.2,817,838),
               CountyInputData('SantaBarabara',446527,11.0,342,385),
               CountyInputData('Nevada',99696,94.5,70,36),
               CountyInputData('Inyo',17987,8.2,20,18),
               CountyInputData('Yuba',78041,100.2,19,16),
               CountyInputData('Butte',231256,27.5,141,16),
               CountyInputData('Sutter',96807,35.3,73,25),
               CountyInputData('Shasta',180040,54.2,130,26),
               CountyInputData('Napa',139417,14.7,136,47),
               CountyInputData('Kings',	151366,4.4,60,28),
               CountyInputData('ElDorodo',190678,33.8,154,36),
               CountyInputData('SanBenito',61537,18.4,19,44),
               CountyInputData('Merced',274765,13.9,121,87),
               CountyInputData('Monterey',435594,9.2,264,136),
               CountyInputData('Marin',259666,27.5,387,189),
               CountyInputData('Imperial',181827, 7.8, 43, 155),
               CountyInputData('Stanislaus',549815,8.1,361,221),
               CountyInputData('Fresno',994400,9.9,664,315),
               CountyInputData('Tulare',465861,8.1,194,397),
               CountyInputData('SanJoaquin',752660,10.6,433,410),
               CountyInputData('Sacramento', 1540975,15.8,1306,914),
               CountyInputData('Madera', 157672,216.7,69,34),
               CountyInputData('Humboldt', 136373,100.4,95,52),
               CountyInputData('SantaCruz', 274255,26.1,276,101),
               CountyInputData('SanLuisObispo', 284010,31.2,235,131)]


input_data = [StateInputData(state='California', county_list=california_county_data)]
