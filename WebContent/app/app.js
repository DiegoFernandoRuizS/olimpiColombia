require('./dependencies.js');
var appConfiguration;
var appModules = [
    'ngCookies',
    'ui.bootstrap',
    'ui.bootstrap.modal',
    'pascalprecht.translate',
    'ngRoute',
    'i18nModule',
    'commonDirectivesModule',
    'commonServicesModule',
    'mainModule',
    'restApiModule',
    'sportListModule'
];

appConfiguration = appConfigurations.productionConfiguration;

angular.module('OlimpiColombiaApp', appModules, appConfiguration);
angular.bootstrap(document, ['OlimpiColombiaApp']);
