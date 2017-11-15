package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import retrofit2.Call;
import retrofit2.Retrofit;

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
        final Button logout = (Button) findViewById(R.id.btn_logout);
        final Button itemCreate = (Button) findViewById(R.id.item_create_btn);

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final SharedPreferences.Editor editor = sharedPref.edit();
        final String  token = sharedPref.getString("TOKEN", null);
        String  username = sharedPref.getString("USERNAME", null);
        String  email = sharedPref.getString("EMAIL", null);
        int  id = sharedPref.getInt("ID", -1);

        itemCreate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
                startActivity(new Intent(getApplicationContext(), ItemCreateActivity.class));
            }
        });

        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Retrofit retrofit = ApiClient.getApiClient();

                ApiInterface apiInterface = retrofit.create(ApiInterface.class);
                Call<JsonResponseSignOut> call = apiInterface.logOut("Token " + token);

                editor.remove("TOKEN");
                editor.remove("USERNAME");
                editor.remove("EMAIL");
                editor.remove("ID");
                editor.commit();

                finish();
                startActivity(new Intent(getApplicationContext(),LoginActivity.class));
            }
        });

        username_text.setText("Welcome " + username + " " + email + " Token = " + token + "ID = " + id );

    }
}
