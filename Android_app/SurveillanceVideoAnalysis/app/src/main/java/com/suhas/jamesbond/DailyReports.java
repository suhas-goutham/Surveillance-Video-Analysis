package com.suhas.jamesbond;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.net.MalformedURLException;
import java.util.HashMap;
import java.util.Map;

public class DailyReports extends AppCompatActivity {

        private Button button1;
        private Button button2;


        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_daily_reports);

            button1 = (Button) findViewById(R.id.people1);
            button2 = (Button) findViewById(R.id.people2);


            button1.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    postData("4a");
                }
            });

            button2.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    postData("4b");
                }
            });
        }

    private void postData(final String option) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                Map<String, String> params = new HashMap<String, String>();
                String post_result = null;
                params.put("option", option);
                try {
                    post_result = HttpUtils.submitPostData(params, "utf-8");
                    Log.d("POST_RESULT", post_result);
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}
