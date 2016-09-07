require('./dependencies.js');
var appConfiguration;
var appModules = [
    'ngCookies',
    'ui.bootstrap',
    'pascalprecht.translate',
    'ngRoute',
    'i18nModule',
    'commonDirectivesModule',
    'mainModule',
    'restApiModule',
    'sportListModule'
];

appConfiguration = appConfigurations.productionConfiguration;

angular.module('OlimpiColombiaApp', appModules, appConfiguration);
angular.bootstrap(document, ['OlimpiColombiaApp']);
