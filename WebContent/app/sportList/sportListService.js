var sportListModule = angular.module('sportListModule');
sportListModule.factory('SportListService', ['SportsApiService', function (SportsApiService) {
    var Sports = function () {
        this.sports = [];
        this.athletesBySport = [];
        this.error = null;
        this.getSports = function () {
            var self = this;
            SportsApiService.loadSports({}, function (response) {
                self.sports = response;
            });
        };

        this.getAthletesBySport = function (sport) {
            var self = this;
            self.athletesBySport = [];
            self.error = null;
            SportsApiService.loadAthletesBySport({sportName: sport.name},
                function (response) {
                    self.athletesBySport = response;
                },
                function (error) {
                    if (error.status = 403) {
                        self.error = error;
                    }
                });
        };
    };
    return new Sports();
}]);
