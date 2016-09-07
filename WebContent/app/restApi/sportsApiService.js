var restApiModule = angular.module('restApiModule');
restApiModule.factory('SportsApiService', ['$resource', function ($resource) {
    return $resource('https://olimpi-colombia.herokuapp.com/api/sports/?format=json', {});
}]);


