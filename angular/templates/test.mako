<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<body>

<script>
var app = angular.module("testApp", []);
app.controller("testCtrl", function($scope, $http) {
    $http.get('${api_uri}', {}).then(function(resp) {
      $scope.data = resp.data;
    });
});
</script>

<div ng-app="testApp" ng-controller="testCtrl">
  <div style="width: 25%">
    <span>
      <div style="font-weight: bold; float: left; margin-right: 5px">Response:</div>
      <div>{{data.data}}</div>
    <span>
    <div style="text-decoration: underline; text-align: center; margin: 20px 0 10px 0">
    Parameters
    </div>
    <div ng-repeat="(key, value) in data.params">
      {{key}} : {{value}}
    </div>
  </div>
  <p>{{errortext}}</p>
</div>
</body>
</html>
