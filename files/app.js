var map;
var mapDiv;
var myOptions;
var locations = [];

function initialize() {
  document.getElementById("geoFindMe").onclick = geoFindMe
  var mapDiv = document.getElementById('map_canvas');

  var myOptions = {
  	center: {lat: 41.070965, lng: -31.099005},
    zoom: 2,
    mapTypeId: google.maps.MapTypeId.TERRAIN
  }
  map = new google.maps.Map(mapDiv, myOptions);

var styles = [
  {
    stylers: [
      { hue: "" },
      { saturation: -40 }
    ]
  },{
    featureType: "road",
    elementType: "geometry",
    stylers: [
      { lightness: 10 },
      { visibility: "simplified" }
    ]
  },{
    featureType: "road",
    elementType: "labels",
    stylers: [
      { visibility: "off" }
    ]
  }
];
map.set({styles: styles});
}

for (i = 0; i < locations.length; i++) {
        size=15;        
        var img=new google.maps.MarkerImage('marker.png',           
            new google.maps.Size(size, size),
            new google.maps.Point(0,0),
            new google.maps.Point(size/2, size/2)
       );

    var marker = new google.maps.Marker({
        map: map,
        title: locations[i].title,
        position: new google.maps.LatLng(locations[i].art_latitude, locations[i].art_longitude),           
            icon: img
    });
}

/// - load google map

function geoFindMe() {
  var output = document.getElementById("out");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;
    console.log(latitude, longitude);

    var currentLoc = new google.maps.LatLng(latitude, longitude)
    map.setCenter(currentLoc)
    map.setZoom(13)

    var marker = new google.maps.Marker({
    position: {lat: latitude, lng: longitude},
    map: map,
    });
    /// - get coordinates, add marker and zoom

  };

  function error() {
    output.innerHTML = "Unable to retrieve your location";
  };

  navigator.geolocation.getCurrentPosition(success, error);
}

/// - Geo Location

var demo = angular.module("demo", [],
  function($interpolateProvider) {
    $interpolateProvider.startSymbol('[!');
    $interpolateProvider.endSymbol('!]');
}) ///

demo.controller('ctrl', function($scope, $http, $filter){ 
  $scope.test = "hello.";

  $scope.fileDetails = 'no';
  $scope.fileSelect = 'yes';
  $scope.login_icon = 'yes';
  $scope.latitude = '';
  $scope.longitude = '';

  $scope.street_photos = [];

  /// - default values

  $http({ method: 'GET', url: '../../list?street_photos' })
    .success(function(data, status) { $scope.street_photos = data; console.log(data);
      $scope.mainImageUrl = $scope.street_photos[0].data_id; });
  $scope.pic_name = '[! item.art_title !]';
  $scope.pic_desc = '[! item.art_about !]';
  
  $scope.setImage = function(item) {
    $scope.mainImageUrl = item.data_id;
  };
  /// - gallery page

  $scope.selectFile = function () { $scope.fileSelect = 'yes'; $scope.fileDetails = 'no'; } 
  $scope.addDetails = function () { $scope.fileSelect = 'no'; $scope.fileDetails  = 'yes'; };
  /// - upload page


  $scope.addCoordinates = function() {
  var output = document.getElementById("out");

    if (!navigator.geolocation){
      output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
      return;
    }

    function success(position) {
      $scope.latitude  = position.coords.latitude;
      $scope.longitude = position.coords.longitude;
      console.log($scope.latitude, $scope.longitude);
    };

    function error() {
      output.innerHTML = "Unable to retrieve your location";
    };

    navigator.geolocation.getCurrentPosition(success, error);
  }

/// - Add geo location to photo


}); /// - ctrl  

