angular.module('emenda.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('SearchCtrl', function($scope) {
  $scope.searchTerm = "";
  $scope.showFilter = false;
  $scope.deputados = [];

  $scope.toggleFilter = function() {
    $scope.showFilter = !$scope.showFilter;
  }
  $scope.search = function() {
    var dept = {
      "id": 1,
      "nome": "Deputado X",
      "partido": "PT",
      "uf": "PB",
      "img": "http://ionicframework.com/img/docs/mcfly.jpg"
    }
    $scope.deputados.push(dept);
  }
})

.controller('ProfileCtrl', function($scope, $http, $stateParams) {
  var convenio = {
    "id": 516457,
    "titulo": "Convenio A"
  };
  $http.get('http://demo1278560.mockable.io/deputado/TIRIRICA_SP')
    .then(function(data) {
      $scope.dept = data.data;
      $scope.dept.convenios = [];
      $scope.dept.convenios.push(convenio);
    }, function(data) {
      //error callback
    });
})

.controller('ConvenioCtrl', function($scope, $stateParams) {
  $scope.convenio = {
    "id": 516457,
    "palavras": [
      {
        "palavra": "Construção",
        "frequencia": 3
      },
      {
        "palavra": "Pavimentação",
        "frequencia": 2
      }
    ]
  }
  $scope.words = [
    { 'word': 'Construção', 'weight': 5},
    { 'word': 'Pavimentação', 'weight': 1},
    { 'word': 'Cabedelo', 'weight': 3},
    { 'word': 'Praia', 'weight': 3}
  ];
});
