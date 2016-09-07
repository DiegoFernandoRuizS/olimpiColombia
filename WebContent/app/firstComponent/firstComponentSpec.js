describe('Module to test: firstComponent', function () {

    beforeEach(module('firstComponentModule'));
    beforeEach(module('pascalprecht.translate'));
    /***
     * Test for directive
     * */
    describe('firstComponent directive', function () {
        var $compile,
            $rootScope;
        beforeEach(inject(function (_$compile_, _$rootScope_) {
            // The injector unwraps the underscores (_) from around the parameter names when matching
            $compile = _$compile_;
            $rootScope = _$rootScope_;
        }));
        it('Replaces the element with the appropriate content', function () {
            // Compile a piece of HTML containing the directive
            var element = $compile('<first-component></first-component>')($rootScope);
            $rootScope.$digest();
            // Check that the compiled element contains the templated content
        });
    });
    /***
     * Test for controller
     * */
    describe('firstComponent Controller', function () {
        var _firstComponentController;

        var _scope;
        it('should be Defined', inject(function ($controller, $rootScope) {
            _scope = $rootScope.$new();
            _firstComponentController = $controller('FirstComponentController', {
            });
            expect(_firstComponentController).toBeDefined();
        }));
    });
    /***
     * Test for service
     * */
    describe('firstComponent Service', function () {

    });
});
