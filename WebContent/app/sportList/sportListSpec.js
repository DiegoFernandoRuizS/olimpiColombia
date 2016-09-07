describe('Module to test: sportList', function () {
   var element;
    beforeEach(module('sportListModule'));
    beforeEach(module('pascalprecht.translate'));
    /***
     * Test for directive
     * */
    describe('sportList directive', function () {
        var $compile,
            $rootScope;
        beforeEach(inject(function (_$compile_, _$rootScope_) {
            // The injector unwraps the underscores (_) from around the parameter names when matching
            $compile = _$compile_;
            $rootScope = _$rootScope_;
        }));
        it('Replaces the element with the appropriate content', function () {
            // Compile a piece of HTML containing the directive
            element = $compile('<sport-list></sport-list>')($rootScope);
            $rootScope.$digest();
            // Check that the compiled element contains the templated content
        });
    });
    /***
     * Test for controller
     * */
    describe('sportList Controller', function () {
        var _sportListController;
        beforeEach(function() {
            _sportListController = element.controller('sportList');
        });
        it('should be Defined', inject(function () {
            expect(_sportListController).toBeDefined();
        }));
    });
    /***
     * Test for service
     * */
    describe('sportList Service', function () {

    });
});
