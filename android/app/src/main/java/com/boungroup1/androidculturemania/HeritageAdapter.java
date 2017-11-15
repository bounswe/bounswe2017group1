package com.boungroup1.androidculturemania;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by tahabayi on 16/11/2017.
 */

public class HeritageAdapter extends RecyclerView.Adapter<HeritageAdapter.MyViewHolder>{

    private ArrayList<JsonResponseHeritage> heritageList;



    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView location, description;

        public MyViewHolder(View view) {
            super(view);
            location = (TextView) view.findViewById(R.id.heritage_location_text);
            description = (TextView) view.findViewById(R.id.heritage_description_text);
        }
    }


    public HeritageAdapter(ArrayList<JsonResponseHeritage> heritageList) {
        this.heritageList = heritageList;
    }

    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.heritage_view, parent, false);

        return new MyViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {

        final JsonResponseHeritage heritageItem = heritageList.get(position);
        holder.location.setText(heritageItem.getLocation());
        holder.description.setText(heritageItem.getDescription());
    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }




}
