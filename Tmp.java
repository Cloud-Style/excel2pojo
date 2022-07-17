package com.test;

import lombok.Data;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonProperty;
    
/**
 * @author majie15
 * @date 2022-07-17
 */
@Data
public class Tmp {
    
    /**
     * 名字
     */
    @JsonAlias("name")
    @JsonProperty("name")
    private String name;
    
    /**
     * 编号
     */
    @JsonAlias("number")
    @JsonProperty("number")
    private String number;
    
    /**
     * 数据推送时间
     */
    @JsonAlias({"publish_date", "publishDate"})
    @JsonProperty("publish_date")
    @JsonFormat(pattern = "yyyy-MM-dd", timezone = "GMT+8")
    private Date publishDate;
    
    /**
     * 年龄
     */
    @JsonAlias("age")
    @JsonProperty("age")
    private Integer age;
    
    /**
     * 有相关关系的朋友
     */
    @JsonAlias("friends")
    @JsonProperty("friends")
    private List friends;
    
    /**
     * 朋友的名字
     */
    @JsonAlias("friends[].name")
    @JsonProperty("friends[].name")
    private String friends[].name;
    
    /**
     * 朋友的年龄
     */
    @JsonAlias("friends[].age")
    @JsonProperty("friends[].age")
    private Integer friends[].age;
        
}
    