Java.perform(function () {
    try {
      var Activity = Java.use('android.app.Activity');
      var ThirdActivity = Java.use('com.example.pwnme.ThirdActivity');
  
      Activity.onCreate.overload('android.os.Bundle').implementation = function (savedInstanceState) {
        // Get the activity class name
        var activityName = this.getClass().getName();
        console.log("Created Activity: " + activityName);
  
        // Call the original method
        this.onCreate(savedInstanceState);
  
        // Check if SecondActivity has been called
        if (activityName === 'com.example.pwnme.SecondActivity') {
          // Now call the onCreate method of ThirdActivity
          var Intent = Java.use('android.content.Intent');
          var intent = Intent.$new(this, Java.use('com.example.pwnme.ThirdActivity').class);
          this.startActivity(intent);
        }
      };
    } catch (error) {
      console.error('Error:', error);
    }
  });
