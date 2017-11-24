package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.support.design.widget.FloatingActionButton;
import android.support.v4.widget.SwipeRefreshLayout;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.Menu;
import android.view.MenuItem;
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

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.item_create_btn);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
                startActivity(new Intent(getApplicationContext(),ItemCreateActivity.class));
            }
        });

        //SwipeRefresh
        final SwipeRefreshLayout swipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.heritage_swipelayout);
        swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refreshHeritageList();
            }
        });

        getHeritageList();

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu,menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final SharedPreferences.Editor editor = sharedPref.edit();
        final String  token = sharedPref.getString("TOKEN", null);
        if (id == R.id.action_logout){
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
        return super.onOptionsItemSelected(item);
    }

    private void refreshHeritageList(){
        new Handler().post(new Runnable() {
            @Override
            public void run() {
                getHeritageList();
                final SwipeRefreshLayout swipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.heritage_swipelayout);
                swipeRefreshLayout.setRefreshing(false);
            };
        });
    }

    private void setHeritageRecyclerView(final ArrayList<JsonResponseHeritage> heritageList){
        final RecyclerView heritageRecyclerView = (RecyclerView) findViewById(R.id.heritage_recycler_view);
        final HeritageAdapter heritageAdapter = new HeritageAdapter(heritageList);

        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(getApplicationContext());
        heritageRecyclerView.setLayoutManager(mLayoutManager);
        heritageRecyclerView.setItemAnimator(new DefaultItemAnimator());
        heritageRecyclerView.setAdapter(heritageAdapter);
        heritageAdapter.notifyDataSetChanged();
        heritageRecyclerView.addOnItemTouchListener(new HeritageRecyclerTouchListener(getApplicationContext(), heritageRecyclerView, new HeritageRecyclerTouchListener.ClickListener() {
            @Override
            public void onClick(View view, int position) {
                JsonResponseHeritage heritage = heritageList.get(position);
                int heritageId= heritage.getId();
                Intent intent = new Intent(getApplicationContext(), ItemDetailView.class);
                intent.putExtra("heritageId",heritageId);
                finish();
                startActivity(intent);
            }

            @Override
            public void onLongClick(View view, int position) {
            }
        }));
    }

    private void getHeritageList(){
        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        Call<List<JsonResponseHeritage>> call = apiInterface.listHeritage();
        call.enqueue(new Callback<List<JsonResponseHeritage>>() {
            @Override
            public void onResponse(Call<List<JsonResponseHeritage>> call, Response<List<JsonResponseHeritage>> response) {
                if (response.isSuccessful()) {
                    final ArrayList<JsonResponseHeritage> heritageList = (ArrayList<JsonResponseHeritage>) response.body();
                    setHeritageRecyclerView(heritageList);
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<List<JsonResponseHeritage>> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down", Toast.LENGTH_SHORT).show();
            }
        });
    }

}
