package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.DividerItemDecoration;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
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

        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        Call<List<JsonResponseHeritage>> call = apiInterface.listHeritage();

        call.enqueue(new Callback<List<JsonResponseHeritage>>() {
            @Override
            public void onResponse(Call<List<JsonResponseHeritage>> call, Response<List<JsonResponseHeritage>> response) {
                if (response.isSuccessful()) {
                    Toast.makeText(getApplicationContext(), "SUCCESS", Toast.LENGTH_SHORT).show();

                    //--
                    //--
                    final RecyclerView heritageView = (RecyclerView) findViewById(R.id.heritage_recycler_view);
                    final HeritageAdapter sAdapter = new HeritageAdapter((ArrayList<JsonResponseHeritage>) response.body());

                    RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(getApplicationContext());



                    heritageView.setLayoutManager(mLayoutManager);
                    heritageView.setItemAnimator(new DefaultItemAnimator());
                    heritageView.setAdapter(sAdapter);
                    DividerItemDecoration dividerItemDecoration = new DividerItemDecoration(heritageView.getContext(),1);
                    heritageView.addItemDecoration(dividerItemDecoration);
                    sAdapter.notifyDataSetChanged();

                    //--
                    //--
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                }

            }

            @Override
            public void onFailure(Call<List<JsonResponseHeritage>> call, Throwable t) {
                Toast.makeText(getApplicationContext(), t.getCause().toString(), Toast.LENGTH_SHORT).show();
            }
        });






        //final TextView username_text = (TextView) findViewById(R.id.username);
        final Button logout = (Button) findViewById(R.id.btn_logout);

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final SharedPreferences.Editor editor = sharedPref.edit();
        final String  token = sharedPref.getString("TOKEN", null);
        String  username = sharedPref.getString("USERNAME", null);
        String  email = sharedPref.getString("EMAIL", null);
        int  id = sharedPref.getInt("ID", -1);

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

        //username_text.setText("Welcome " + username + " " + email + " Token = " + token + "ID = " + id );

    }
}
