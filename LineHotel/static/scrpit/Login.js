var userID,userName;
$(document).ready(function(){
  
    liff.init({liffId:"***************"});
    if (!liff.isLoggedIn()) {
        liff.login();
      }else{
        window.location.href='/hotelBoss/user_data.html';
      }
    liff.getProfile().then(function (profile) {
      userID=profile.userId;
      userName=profile.displayName;
  }).catch(function (error) {
      console.log('error', err);
  });
});