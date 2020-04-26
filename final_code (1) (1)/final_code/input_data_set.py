import typing as ty


class CountyInputData:
    def __init__(self, name: str, population: int, doubling_rate: float, doctor_count: int, infected_population: int):
        self.name = name,
        self.population = population
        self.doubling_rate_days = doubling_rate
        self.num_doctor = doctor_count
        self.infected_population = infected_population


class StateInputData:
    def __init__(self, name: str, county_data: ty.List):
        self.name = name
        self.county_data = county_data

    def get_county_data(self):
        return self.county_data


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

florida_county_data = [
                    CountyInputData('Bay', 185287, 13.5, 100, 55),
                    CountyInputData('Bradford', 27732, 11.5, 8, 42),
                    CountyInputData('Brevard', 596849, 10, 434, 215),
                    CountyInputData('Broward', 1951260, 17, 1420, 3971),
                    CountyInputData('Charlotte', 184998, 24.5, 117, 138),
                    CountyInputData('Citrus', 147929, 28, 75, 84),
                    CountyInputData('Clay', 216072, 12.5, 104, 247),
                    CountyInputData('Collier', 378488, 18, 279, 463),
                    CountyInputData('Columbia', 70503, 11.5, 32, 39),
                    CountyInputData('Duval', 950181, 19, 807, 854),
                    CountyInputData('Escambia', 315534, 14.5, 213, 309),
                    CountyInputData('Flager', 112067, 9.5, 56, 75),
                    CountyInputData('Gadsden', 45894, 6, 9, 51),
                    CountyInputData('Hendry', 41556, 6.5, 13, 41),
                    CountyInputData('Hernando', 190865, 23.5, 106, 84),
                    CountyInputData('Highlands', 105424, 27, 61, 70),
                    CountyInputData('Hillsborough', 1436888, 21.5, 1170, 960),
                    CountyInputData('Jefferson', 14288, 5.5, 3, 26),
                    CountyInputData('Lake', 356495, 15, 243, 207),
                    CountyInputData('Lee', 754610, 24.5, 479, 769),
                    CountyInputData('Leon', 292502, 15.5, 251, 176),
                    CountyInputData('Madison', 18529, 10.5, 2, 21),
                    CountyInputData('Manatee', 394855, 9, 214, 417),
                    CountyInputData('Marion', 359977, 19.5, 204, 121),
                    CountyInputData('Martin', 160912, 24, 106, 151),
                    CountyInputData('Miami-Dade', 2761581, 18, 2181, 9354),
                    CountyInputData('Monroe', 75027, 25, 59, 73),
                    CountyInputData('Nassau', 85832, 17.5, 39, 44),
                    CountyInputData('Okaloosa', 207269, 16.5, 161, 131),
                    CountyInputData('Orange', 1380645, 22, 1179, 1198),
                    CountyInputData('Osceola', 367990, 19.5, 144, 409),
                    CountyInputData('Palm Beach', 1485941, 16, 1165, 2170),
                    CountyInputData('Pasco', 539630, 21, 308, 205),
                    CountyInputData('Pinellas', 975280, 17.5, 856, 592),
                    CountyInputData('Polk', 708009, 19.5, 336, 326),
                    CountyInputData('Putnam', 74163, 15, 32, 56),
                    CountyInputData('Santa Rosa', 179349, 20, 124, 138),
                    CountyInputData('Sarasota', 426718, 19.5, 319, 284),
                    CountyInputData('Seminole', 467832, 20.5, 350, 320),
                    CountyInputData('St. Lucie', 321128, 16.5, 120, 202),
                    CountyInputData('Sumter', 128754, 17, 47, 147),
                    CountyInputData('Suwannee', 44191, 15, 7, 98),
                    CountyInputData('Volusia', 547538, 10.5, 370, 333)]


input_data = [StateInputData(name='California', county_data=california_county_data),
              StateInputData(name='Florida', county_data=florida_county_data)]
