var userID,userName;
$(document).ready(function(){
  var fst=setInterval(function(){
    
    liff.init({liffId:"1654463147-DN3l43MN"}); 

    liff.getProfile().then(function (profile) {
      userID=profile.userId;
      userName=profile.displayName;
      clearInterval(fst);
  }).catch(function (error) {
      console.log('error', err);
  });

  },1000);
    
});