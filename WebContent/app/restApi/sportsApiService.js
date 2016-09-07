var restApiModule = angular.module('restApiModule');
restApiModule.factory('SportsApiService', ['$resource', function ($resource) {
    return $resource('api/sports', {}, {
        loadSports: {
            url: 'api/sports/?format=json',
            method: 'GET',
            isArray: true,
            params: {}
        }
    });
}]);
