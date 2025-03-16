let loaded_pages = {};
let search_dicts = {};
let cur_page = null;
let cur_search_dict = [];

function OnNavBtn1Clicked(p)
{
    elem = document.getElementById(p);
    elem.setAttribute("active", "false")
    for(node of elem.children)
    {
        if(node.className == "navbtn child")
        {
            node.hidden = !node.hidden

        }
    }
}

function OpenPage(name)
{
    if(cur_page)
    {
        cur_page.setAttribute("active", "false");
    }
    
    if(!(name in loaded_pages))
    {
        LoadPage(name);
    }
    else
    {
        cur_page = loaded_pages[name];
        cur_search_dict = search_dicts[name];
    }
    cur_page.setAttribute("active", "true");
}
function LoadPage(name)
{
    elem = document.createElement("div");
    elem.className = "page"
    document.getElementById("main").appendChild(elem);
    cur_page = elem;
    cur_search_dict = [];

    loaded_pages[name] = cur_page;
    search_dicts[name] = cur_search_dict;
    LoadStart(name);
    
}

function OnLoad()
{
    loaded_pages["Credit"] = document.getElementById("credit");
    search_dicts["Credit"] = []
    OnResize();
}
function OnResize()
{
    emsize = parseFloat(getComputedStyle(document.body).fontSize);
    if(document.body.clientWidth > emsize * 70)
        document.getElementById("actualbody").style.width = "70em";
    else
        document.getElementById("actualbody").style.width = "100%";


    if(document.getElementById("actualbody").clientWidth < emsize * 50)
        document.getElementById("main").style.width = "50em";
    else
        document.getElementById("main").style.width = "100%";
}

