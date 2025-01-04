Java.perform(function () {
    try {
      var Activity = Java.use('android.app.Activity');
  
      Activity.onCreate.overload('android.os.Bundle').implementation = function (savedInstanceState) {
        // Get the activity class name
        var activityName = this.getClass().getName();
        console.log("Created Activity: " + activityName);
  
        // Call the original method
        this.onCreate(savedInstanceState);
      };
      
    } catch (error) {
      console.error('Error:', error);
    }
  });
