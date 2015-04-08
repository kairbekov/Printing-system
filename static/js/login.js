/**
 * Created by abuka on 07.04.2015.
 */
angular.module('loginApplication',[])
.controller('LoginController', ['$scope', '$http',
	function($scope, $http){

		$scope.text = "";
		$scope.url = "http://127.0.0.1/mainapp/login/";
		$scope.params = {
			username : "",
			password : ""
		};
		$scope.data = "";
		$scope.status = "";


		$scope.loginBtn = function(){
			$http({method: 'GET', url: $scope.url, params: $scope.params}).
	        success(function(data, status) {
	          $scope.status = status;
	          $scope.data = data;
	        }).
	        error(function(data, status) {
	          $scope.data = data || "Request failed";
	          $scope.status = status;
	      	});
		};

}]);
