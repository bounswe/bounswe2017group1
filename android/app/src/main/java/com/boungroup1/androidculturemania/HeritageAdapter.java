package com.boungroup1.androidculturemania;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

import de.hdodenhof.circleimageview.CircleImageView;

/**
 * Created by tahabayi on 16/11/2017.
 */

public class HeritageAdapter extends RecyclerView.Adapter<HeritageAdapter.MyViewHolder>{

    private ArrayList<JsonResponseHeritage> heritageList;
    private Context mContext;



    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView title, description, location, creator_username ;
        private CircleImageView item_avatar;

        public MyViewHolder(View view) {
            super(view);
            title = (TextView) view.findViewById(R.id.heritage_title_text);
            description = (TextView) view.findViewById(R.id.heritage_description_text);
            location = (TextView) view.findViewById(R.id.heritage_location_text);
            creator_username = (TextView) view.findViewById(R.id.heritage_creator_username_text);
            item_avatar = (CircleImageView) view.findViewById(R.id.item_avatar);
        }
    }


    public HeritageAdapter(Context context,ArrayList<JsonResponseHeritage> heritageList) {
        this.mContext = context;
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
        //Render image using Picasso library
        if (!TextUtils.isEmpty(heritageItem.getCreator_image_path())) {
            Log.d("IMAGE_PATH",ApiClient.BASE_URL+heritageItem.getCreator_image_path());
            Picasso.with(mContext).load(ApiClient.BASE_URL+heritageItem.getCreator_image_path())
                    .error(R.drawable.avatar)
                    .placeholder(R.drawable.avatar)
                    .into(holder.item_avatar);
        }


        holder.title.setText(heritageItem.getTitle());
        holder.description.setText(heritageItem.getDescription());
        holder.location.setText(heritageItem.getLocation());
        holder.creator_username.setText("By " + heritageItem.getCreator_username());



    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }

}
