package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onStart() {
        super.onStart();
        SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        String  token = sharedPref.getString("TOKEN", null);
        Intent intent = new Intent(this, SingUpActivity.class);
        if (token == null){
            finish();
            startActivity(intent);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final TextView username_text = (TextView) findViewById(R.id.username);
        SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        String  token = sharedPref.getString("TOKEN", null);
        String  username = sharedPref.getString("USERNAME", null);
        String  email = sharedPref.getString("EMAIL", null);
        int  id = sharedPref.getInt("ID", -1);


        username_text.setText("Welcome " + username + " " + email + " Token = " + token + "ID = " + id );

    }
}
