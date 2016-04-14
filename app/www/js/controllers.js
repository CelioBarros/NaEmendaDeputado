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

.controller('SearchCtrl', function($scope, $http) {
  $scope.searchTerm = {
    term: "",
    isSearching: false,
    isLoading: false
  };
  $scope.showFilter = false;
  $scope.deputados = [];

  $scope.toggleFilter = function() {
    $scope.showFilter = !$scope.showFilter;
  }
  $scope.startSearch = function() {
    $scope.searchTerm.isSearching = true;
  }
  $scope.stopSearch = function() {
    $scope.searchTerm.isSearching = false;
  }
  $scope.search = function() {
    $scope.searchTerm.isLoading = true;
    $http.get('http://naemendadosdeputados-celiobarros.rhcloud.com/api/busca/'+$scope.searchTerm.term)
      .then(function(response) {
        $scope.deputados = response.data;
        $scope.searchTerm.isLoading = false;
      });
  }
})

.controller('ProfileCtrl', function($scope, $http, $stateParams) {
  var id_deputado = $stateParams.id_deputado;
  $http.get('http://naemendadosdeputados-celiobarros.rhcloud.com/api/deputado/'+id_deputado)
    .then(function(response) {
      $scope.dept = response.data;
    }, function(data) {});
  $http.get('http://naemendadosdeputados-celiobarros.rhcloud.com/api/deputado/'+id_deputado+'/convenios')
    .then(function(response) {
      $scope.dept.convenios = response.data;
    }, function(data) {});
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
