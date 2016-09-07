var restApiModule = angular.module('restApiModule');
restApiModule.factory('SportsApiService', ['$resource', function ($resource) {
    return $resource('api/sports', {}, {
        loadSports: {
            url: 'https://olimpi-colombia.herokuapp.com/api/sports/?format=json',
            method: 'GET',
            isArray: true,
            params: {}
        },

        loadAthletesBySport: {
            url: 'https://olimpi-colombia.herokuapp.com/api/athletes_by_sport/:sportName/?format=json',
            method: 'GET',
            isArray: true,
            params: {sportName:''}
        }
    });
}]);
