function LoadStart(name)
{
    fetch('data/' + name + '.json')
    .then((response) => response.json())
    .then((json) => LoadOffset(name, json));
}

function LoadOffset(name, json)
{
    search_dict = search_dicts[name]
    load_page = loaded_pages[name]

    summary = json["summary"]
    large_offset = summary["large_offset"]
    elem = document.createElement("p");
    elem.className = "title";
    elem.innerHTML = summary["name"]
    cur_page.appendChild(elem)

    elem = document.createElement("div");
    elem.className = "inputbox";
    elem.innerHTML = '<input id="' + name + '_search" type="text"  placeholder="Search" oninput="TextInput(\'' + name + '\')"/>'
    cur_page.appendChild(elem)

    table = document.createElement("div");
    table.className = "items";

    for (item of json["data"])
    {
        elem = document.createElement("div");
        if(item.hasOwnProperty("uniongroup"))
        {
            elem.className = "itembox uniongroup";
            elem.setAttribute("name", "u_" + item["uniongroup"]);
        }
        else if(item.hasOwnProperty("unionof"))
        {
            elem.className = "itembox unionof";
            elem.setAttribute("name", "i_" + item["unionof"])
            elem.setAttribute("unioncollapse", "true");
        }
        else
        {
            elem.className = "itembox";
        }
        elem.addEventListener("click", OnClickItem);
        
        elem2 = document.createElement("div");
        elem2.className = "summbox"

        if ("offset" in item)
        {
            p = document.createElement("p");
            if(large_offset)
                p.className = "item address large";
            else
                p.className = "item address";
            p.innerHTML = item["offset"];
            elem2.appendChild(p);
        }
        if ("size" in item)
        {
            p = document.createElement("p");
            if(large_offset)
                p.className = "item datasize large";
            else
                p.className = "item datasize";
            if (item["length"] == 1)
                p.innerHTML = item["size"];
            else
                p.innerHTML =  item["length"] + "×" + item["size"];
            elem2.appendChild(p);
        }
        if ("varname" in item)
        {
            p = document.createElement("p");
            p.className = "item varname";
            p.innerHTML = item["varname"];
            elem2.appendChild(p);
        }
        p = document.createElement("p");
        p.className = "item name";
        p.innerHTML = item["name"];
        elem2.appendChild(p);
        if ("scr" in item)
        {
            scr = item["scr"];
            if (scr == "Supported" || scr == "Simple Data")
                support_color = "#afa";
            else if(scr == "Backed By Code" || scr == "Read Only")
                support_color = "#ff8";
            else if(scr == "Unsupported")
                support_color = "#f88";
            else
                support_color = "#fff";
            
            p = document.createElement("p");
            p.className = "item support";
            p.innerHTML = scr;
            p.style.color = support_color
            elem2.appendChild(p);
        }
        elem.appendChild(elem2);


        elem2 = document.createElement("div");
        elem2.className = "descbox"
        elem2.setAttribute("hidden", "true")
        p = document.createElement("p");
        p.className = "item description";
        p.innerHTML = item["description"];
        elem2.appendChild(p);
        elem.appendChild(elem2);
        
        table.appendChild(elem);
        key = item["name"].toLowerCase()
        search_dict.push([key, elem])
    }
    load_page.appendChild(table)
}
function ReadTranslatable(item, name, parent)
{
    en = "";
    kr = "";
    if(typeof item == 'string')
    {
        en = item
        kr = ""
    }
    else
    {
        if ("en" in item)
            en = item["en"]
        if ("kr" in item)
            kr = item["kr"]
    }
    p = document.createElement("p");
    p.className = "item " + name + " " + "english";
    p.innerHTML = en;
    parent.appendChild(p);

    p = document.createElement("p");
    p.className = "item " + name + " " + "korean";
    p.innerHTML = kr;
    parent.appendChild(p);

    if (name == "name")
        return en + kr
}