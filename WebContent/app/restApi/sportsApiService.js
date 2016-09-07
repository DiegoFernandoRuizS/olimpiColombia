var restApiModule = angular.module('restApiModule');
restApiModule.factory('SportsApiService', ['$resource', function ($resource) {
    return $resource('api/sports/?format=json', {});
}]);


