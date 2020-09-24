package com.suhas.jamesbond;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.net.MalformedURLException;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        button1=(Button)findViewById(R.id.opp1);
        button2=(Button)findViewById(R.id.opp2);
        button3=(Button)findViewById(R.id.opp3);
        button4=(Button)findViewById(R.id.opp4);

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(MainActivity.this, VehicleCounting.class);
                MainActivity.this.startActivity(myIntent);
            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(MainActivity.this, PeopleCounting.class);
                MainActivity.this.startActivity(myIntent);
            }
        });

        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                postData("3");
            }
        });

        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(MainActivity.this, DailyReports.class);
                MainActivity.this.startActivity(myIntent);
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