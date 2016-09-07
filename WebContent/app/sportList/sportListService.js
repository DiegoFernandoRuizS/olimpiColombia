var sportListModule = angular.module('sportListModule');
sportListModule.factory('SportListService', ['SportsApiService',function (SportsApiService) {
        var Sports = function () {
            var _self = {}; //private
            _self.sports = [];

            this.getSports = function () {
                 var self = this;
                console.log('sucede');
                SportsApiService.get({}, function (response) {
                    console.log('esto sucede', response);
                });
            };

        };
        return new Sports();
    }]);
