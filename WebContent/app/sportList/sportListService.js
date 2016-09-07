var sportListModule = angular.module('sportListModule');
sportListModule.factory('SportListService', ['SportsApiService', function (SportsApiService) {
    var Sports = function () {
        this.sports = [];
        this.athletesBySport = [];
        this.getSports = function () {
            var self = this;
            SportsApiService.loadSports({}, function (response) {
                self.sports = response;
            });
        };

        this.getAthletesBySport = function (sport) {
            var self = this;
            self.athletesBySport = [];
            SportsApiService.loadAthletesBySport({sportName: sport.name}, function (response) {
                self.athletesBySport = response;
            });
        };
    };
    return new Sports();
}]);
