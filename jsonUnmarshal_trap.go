

func TestJsonMarshal(t *testing.T) {
	var data interface{}
	var emptyMap map[string]string
	data = emptyMap
	if data != nil {
		msg, err := json.Marshal(data)
		fmt.Println("TestJsonmarshal:", len(msg), data, string(msg), emptyMap == nil, err) // 4, map[], "null", true, nil
	}
	
	//marshal nil map will got "null" 
	msg, err := json.Marshal(emptyMap)
	fmt.Println("TestJsonmarshal:", len(msg), string(msg), msg, err) // 4, "null", [110 117 108 108],  nil

	nulljson := []byte("null")
	require.Equal(t, string(msg), string(nulljson))
	require.Equal(t, string(msg), "null")

	// err = json.Unmarshal(msg, &data)
	// fmt.Println(err, data) //nil,nil

	//case1: parse "null"  will got nil map
	err = json.Unmarshal([]byte("null"), &emptyMap)
	fmt.Println(err, emptyMap) //nil, map[]
	require.Equal(t, true, nil == emptyMap)
	// emptyMap["a"] = "b" //panic due to nil map

	//case2: parse "{}" will got valid map
	var emptyMap2 map[string]string
	err = json.Unmarshal([]byte(`{}`), &emptyMap2)
	fmt.Println(err, emptyMap2["a"] == "") //nil, true
	require.Equal(t, true, nil != emptyMap2)
	emptyMap2["a"] = "b" //ok, no panic due to

	//case3: parse "invalidJson" will got error.
	err = json.Unmarshal([]byte("notJsonString"), &emptyMap)
	require.NotNil(t, err) //err = invalid character 'o' in literal null

	//case4: parse valid json string got valid map
	err = json.Unmarshal([]byte(`{"a":"b"}`), &emptyMap)
	require.Equal(t, "b", emptyMap["a"]) //nil, b
	require.Equal(t, nil, err)

}
