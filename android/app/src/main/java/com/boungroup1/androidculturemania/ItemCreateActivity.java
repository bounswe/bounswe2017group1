package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

//import static android.R.attr.password;
//import static com.boungroup1.androidculturemania.R.id.username;

/**
 * Created by user on 15/11/2017.
 */

public class ItemCreateActivity extends AppCompatActivity{

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item_create);
        final EditText title = (EditText) findViewById(R.id.input_title);
        final EditText description = (EditText) findViewById(R.id.input_description);
        final EditText location = (EditText) findViewById(R.id.input_location);
        final EditText tags = (EditText) findViewById(R.id.tags);
        final Button btn_create_item = (Button) findViewById(R.id.btn_create_item);

        btn_create_item.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String title_str = title.getText().toString().trim();
                String description_str = description.getText().toString().trim();
                String location_str = location.getText().toString().trim();

                if (!TextUtils.isEmpty(title_str) && !TextUtils.isEmpty(description_str) && !TextUtils.isEmpty(location_str))
                {
                    sendPost(title_str, description_str, location_str);
                }
            }
        });

    }

    public void sendPost(final String title, final String description, final String location){
        Retrofit retrofit = ApiClient.getApiClient();
        String date = new SimpleDateFormat("dd-MM-yyyy").format(new Date());
        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        Tag[] tagsArray = new Tag[2];
        tagsArray[0] = new Tag("new", "cat");
        tagsArray[1] = new Tag("secnew", "seccat");
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseItemCreate> call = apiInterface.itemCreate(new ItemCreateBody(title, description, "2012-09-04 06:00:00.000000", location,tagsArray ),"Token " + token);
        call.enqueue(new Callback<JsonResponseItemCreate>() {
            @Override
            public void onResponse(Call<JsonResponseItemCreate> call, Response<JsonResponseItemCreate> response) {

                if (response.isSuccessful()) {

                    Toast.makeText(getApplicationContext(), "SUCCESS", Toast.LENGTH_SHORT).show();
//                    Log.d("RESPONSE", response.body().getProfile().getGender());
//                    openMain(response.body().getToken(), response.body().getProfile().getUsername(),
//                            response.body().getUser().getEmail(),
//                            response.body().getProfile().getId());
                    finish();
                    startActivity(new Intent(getApplicationContext(), MainActivity.class));
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                    Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseItemCreate> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
