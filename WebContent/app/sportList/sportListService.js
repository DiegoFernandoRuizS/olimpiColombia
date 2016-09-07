var sportListModule = angular.module('sportListModule');
sportListModule.factory('SportListService', ['SportsApiService', function (SportsApiService) {
    var Sports = function () {
        this.sports = [];
        this.sportSelected ={};
        this.getSports = function () {
            var self = this;
            SportsApiService.loadSports({}, function (response) {
                self.sports = response;
            });
        };
    };
    return new Sports();
}]);
